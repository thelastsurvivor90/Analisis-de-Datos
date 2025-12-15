"""
Script para descargar automáticamente el Bank Marketing Dataset
desde el repositorio UCI Machine Learning
"""

import os
import requests
import zipfile
from pathlib import Path

def create_data_folder():
    """Crear carpeta data/ si no existe"""
    data_folder = Path("data")
    if not data_folder.exists():
        data_folder.mkdir()
        print("✓ Carpeta 'data/' creada")
    else:
        print("✓ Carpeta 'data/' ya existe")
    return data_folder

def download_dataset():
    """Descargar el dataset desde UCI"""
    print("\n" + "="*70)
    print("DESCARGA DEL BANK MARKETING DATASET")
    print("="*70 + "\n")
    
    # URL del dataset
    url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
    
    # Crear carpeta data
    data_folder = create_data_folder()
    
    # Nombre del archivo
    zip_filename = data_folder / "bank_marketing.zip"
    
    try:
        print(f"Descargando desde: {url}")
        print("Por favor espera, esto puede tomar unos minutos...")
        
        # Descargar con barra de progreso
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        downloaded = 0
        
        with open(zip_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=block_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    # Mostrar progreso
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\rProgreso: {percent:.1f}% ({downloaded}/{total_size} bytes)", end='')
        
        print("\n✓ Descarga completada")
        
        # Extraer archivos
        print("\nExtrayendo archivos...")
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(data_folder)
        
        print("✓ Archivos extraídos")
        
        # Buscar el archivo principal
        csv_files = list(data_folder.glob("**/*.csv"))
        
        if csv_files:
            print(f"\n✓ Dataset descargado exitosamente en: {data_folder}")
            print("\nArchivos disponibles:")
            for csv_file in csv_files:
                size_mb = csv_file.stat().st_size / (1024 * 1024)
                print(f"  - {csv_file.name} ({size_mb:.2f} MB)")
            
            # Encontrar el archivo full
            full_csv = [f for f in csv_files if 'full' in f.name.lower()]
            if full_csv:
                print(f"\n📊 Archivo principal: {full_csv[0].name}")
                print(f"📍 Ruta: {full_csv[0]}")
        
        # Limpiar archivo zip
        if zip_filename.exists():
            zip_filename.unlink()
            print("\n✓ Archivo temporal eliminado")
        
        print("\n" + "="*70)
        print("¡DESCARGA COMPLETADA CON ÉXITO!")
        print("="*70)
        print("\nPuedes ejecutar el análisis con:")
        print("  python analisis_probabilidad.py")
        print("="*70 + "\n")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"\n✗ Error al descargar: {e}")
        print("\nIntenta descargar manualmente desde:")
        print("https://archive.ics.uci.edu/dataset/222/bank+marketing")
        return False
    
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}")
        return False

def verify_dataset():
    """Verificar si el dataset ya existe"""
    data_folder = Path("data")
    
    if not data_folder.exists():
        return False
    
    csv_files = list(data_folder.glob("**/*.csv"))
    
    if csv_files:
        print("\n✓ Dataset ya existe en la carpeta 'data/'")
        print("\nArchivos encontrados:")
        for csv_file in csv_files:
            size_mb = csv_file.stat().st_size / (1024 * 1024)
            print(f"  - {csv_file.name} ({size_mb:.2f} MB)")
        
        response = input("\n¿Deseas descargar nuevamente? (s/N): ").strip().lower()
        return response != 's'
    
    return False

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║         DESCARGADOR DE BANK MARKETING DATASET (UCI)             ║
    ║                                                                  ║
    ║  Este script descarga automáticamente el dataset desde el       ║
    ║  repositorio UCI Machine Learning Repository                    ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
    """)
    
    # Verificar si ya existe
    if not verify_dataset():
        # Descargar
        success = download_dataset()
        
        if not success:
            print("\n💡 ALTERNATIVAS:")
            print("   1. Descarga manual: https://archive.ics.uci.edu/dataset/222/bank+marketing")
            print("   2. Usar dataset simulado (ya incluido en el código)")
            print("   3. Intentar nuevamente más tarde")
    else:
        print("\n✓ Todo listo! Puedes ejecutar el análisis.")
        print("\nComando:")
        print("  python analisis_probabilidad.py")
