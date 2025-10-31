#!/usr/bin/env python3
# ?? ???? Cursor AI ????? ?????? ComfyUI ????????

import os
import sys
import time
import json
import subprocess
import psutil
import requests
from datetime import datetime
from pathlib import Path

class ComfyUIAgent:
    """???? ??? ??????? ?????? ComfyUI"""
    
    def __init__(self, comfyui_dir, host="localhost", port=8188):
        self.comfyui_dir = Path(comfyui_dir)
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}"
        self.process = None
        self.log_file = Path(__file__).parent.parent / "logs" / "agent.log"
        self.log_file.parent.mkdir(exist_ok=True)
        
    def log(self, message, level="INFO"):
        """????? ????? ?? ?????"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] [{level}] {message}"
        print(log_msg)
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_msg + '\n')
    
    def check_health(self):
        """?????? ?? ??? ??????"""
        try:
            response = requests.get(f"{self.base_url}/system_stats", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def start_comfyui(self):
        """??? ???? ComfyUI"""
        if self.is_running():
            self.log("ComfyUI ???? ??????", "INFO")
            return True
        
        self.log("??? ComfyUI...", "INFO")
        
        try:
            venv_python = self.comfyui_dir / "venv" / "bin" / "python"
            main_py = self.comfyui_dir / "main.py"
            
            self.process = subprocess.Popen(
                [str(venv_python), str(main_py), "--listen", "--port", str(self.port)],
                cwd=str(self.comfyui_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # ?????? ??? ???? ??????
            for _ in range(30):
                time.sleep(2)
                if self.check_health():
                    self.log("? ComfyUI ??? ?????", "SUCCESS")
                    return True
            
            self.log("?? ComfyUI ??? ??? ?? ?????", "WARNING")
            return False
            
        except Exception as e:
            self.log(f"? ??? ??? ComfyUI: {str(e)}", "ERROR")
            return False
    
    def stop_comfyui(self):
        """????? ???? ComfyUI"""
        if self.process:
            self.log("????? ComfyUI...", "INFO")
            self.process.terminate()
            self.process.wait(timeout=10)
            self.log("? ?? ????? ComfyUI", "SUCCESS")
    
    def is_running(self):
        """?????? ??? ??? ComfyUI ????"""
        return self.check_health()
    
    def restart_comfyui(self):
        """????? ????? ComfyUI"""
        self.log("????? ????? ComfyUI...", "INFO")
        self.stop_comfyui()
        time.sleep(3)
        return self.start_comfyui()
    
    def get_system_stats(self):
        """?????? ??? ???????? ??????"""
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return {
            "cpu": cpu_percent,
            "memory": {
                "total": memory.total / (1024**3),  # GB
                "used": memory.used / (1024**3),
                "percent": memory.percent
            },
            "disk": {
                "total": disk.total / (1024**3),
                "used": disk.used / (1024**3),
                "percent": disk.percent
            }
        }
    
    def monitor(self, interval=60):
        """?????? ??????"""
        self.log("?? ??? ???????? ????????...", "INFO")
        
        while True:
            try:
                if not self.is_running():
                    self.log("?? ComfyUI ?? ????! ?????? ????? ???????...", "WARNING")
                    self.start_comfyui()
                
                stats = self.get_system_stats()
                
                # ??????? ???????
                if stats['memory']['percent'] > 90:
                    self.log(f"?? ??????? ??????: {stats['memory']['percent']}%", "WARNING")
                
                if stats['disk']['percent'] > 90:
                    self.log(f"?? ????? ?????: {stats['disk']['percent']}%", "WARNING")
                
                self.log(f"? ??????: CPU={stats['cpu']}% MEM={stats['memory']['percent']}%", "INFO")
                
                time.sleep(interval)
                
            except KeyboardInterrupt:
                self.log("????? ????????...", "INFO")
                break
            except Exception as e:
                self.log(f"? ??? ?? ????????: {str(e)}", "ERROR")
                time.sleep(interval)
    
    def cleanup_old_outputs(self, days=7):
        """????? ???????? ???????"""
        output_dir = self.comfyui_dir / "output"
        if not output_dir.exists():
            return
        
        self.log(f"?? ????? ??????? ?????? ?? {days} ????...", "INFO")
        
        cutoff = time.time() - (days * 86400)
        deleted = 0
        
        for file in output_dir.rglob("*"):
            if file.is_file() and file.stat().st_mtime < cutoff:
                file.unlink()
                deleted += 1
        
        self.log(f"? ?? ??? {deleted} ???", "SUCCESS")
    
    def backup_workflows(self):
        """??? ??????? ??? workflows"""
        workflows_dir = self.comfyui_dir / "workflows"
        if not workflows_dir.exists():
            return
        
        backup_dir = Path(__file__).parent.parent / "backups" / datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        self.log(f"?? ??? ??????? ??? workflows...", "INFO")
        
        import shutil
        shutil.copytree(workflows_dir, backup_dir / "workflows")
        
        self.log(f"? ?? ????? ??: {backup_dir}", "SUCCESS")


def main():
    """?????? ????????"""
    import argparse
    
    parser = argparse.ArgumentParser(description='?? ???? Cursor AI ?????? ComfyUI')
    parser.add_argument('--comfyui-dir', required=True, help='???? ComfyUI')
    parser.add_argument('--action', choices=['start', 'stop', 'restart', 'monitor', 'cleanup', 'backup'], 
                        default='monitor', help='??????? ???????')
    parser.add_argument('--interval', type=int, default=60, help='???? ???????? ????????')
    
    args = parser.parse_args()
    
    agent = ComfyUIAgent(args.comfyui_dir)
    
    if args.action == 'start':
        agent.start_comfyui()
    elif args.action == 'stop':
        agent.stop_comfyui()
    elif args.action == 'restart':
        agent.restart_comfyui()
    elif args.action == 'monitor':
        agent.monitor(args.interval)
    elif args.action == 'cleanup':
        agent.cleanup_old_outputs()
    elif args.action == 'backup':
        agent.backup_workflows()


if __name__ == '__main__':
    main()
