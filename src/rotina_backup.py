"""
Rotina Automatizada de Backup & Log de Execução
Autor: Fabrício Oliveira Silva
Descrição: Utilitário em Python para compactação e cópia de segurança com registro de logs estruturados.
"""

import os
import zipfile
import logging
from datetime import datetime


def configurar_logger(logs_dir: str = "logs") -> logging.Logger:
    """Configura o sistema de log registrando eventos na pasta /logs"""
    os.makedirs(logs_dir, exist_ok=True)
    log_file = os.path.join(logs_dir, f"backup_{datetime.now().strftime('%Y%m%d')}.log")
    
    logger = logging.getLogger("DevOpsBackup")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        handler = logging.FileHandler(log_file, encoding='utf-8')
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger


def executar_backup_diretorio(origem_dir: str, destino_zip: str) -> bool:
    """Compacta a pasta de origem gerando um arquivo .zip de segurança"""
    logger = configurar_logger()
    logger.info(f"Iniciando rotina de backup da pasta: {origem_dir}")
    
    try:
        if not os.path.exists(origem_dir):
            logger.error(f"Diretório de origem não encontrado: {origem_dir}")
            return False
            
        with zipfile.ZipFile(destino_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(origem_dir):
                for file in files:
                    filepath = os.path.join(root, file)
                    arcname = os.path.relpath(filepath, origem_dir)
                    zipf.write(filepath, arcname)
                    
        logger.info(f"Backup concluído com sucesso: {destino_zip}")
        return True
    except Exception as e:
        logger.error(f"Falha durante a execução do backup: {str(e)}")
        return False


if __name__ == "__main__":
    print("=== EXECUTANDO ROTINA DE BACKUP DEVOPS ===")
    status = executar_backup_diretorio("data", "data_backup.zip")
    print(f"Resultado do Backup: {'SUCESSO' if status else 'FALHA (Verifique os logs na pasta /logs)'}")
