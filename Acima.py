import ctypes
import tempfile
import os
import subprocess
import sys

# 1. Mudamos de float para double para garantir precisão de 3 casas decimais
codigo_c = """
#include <stdio.h>

void calcular(int N, int* notas, double* percentual) {
    long long soma = 0; // Usar long long para evitar overflow em somas grandes
    int acima = 0;
    double media;
    
    for (int i = 0; i < N; i++) {
        soma += notas[i];
    }

    media = (double)soma / N;

    for (int i = 0; i < N; i++) {
        if ((double)notas[i] > media) {
            acima++;
        }
    }

    *percentual = (acima * 100.0) / N;
}
"""

# ... (processo de compilação temporária permanece igual) ...
tmp_c = tempfile.NamedTemporaryFile(suffix='.c', delete=False, mode='w')
tmp_c.write(codigo_c)
tmp_c.close()
tmp_so = tmp_c.name.replace('.c', '.so')

subprocess.run(['gcc', '-shared', '-fPIC', '-o', tmp_so, tmp_c.name], check=True)
lib = ctypes.CDLL(tmp_so)

# 2. Atualizando os tipos para c_double
lib.calcular.argtypes = [
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_double) # Alterado para double
]

# 3. Função para ler entrada de forma robusta (lida com quebras de linha)
def get_input():
    for line in sys.stdin:
        for word in line.split():
            yield word

input_generator = get_input()

try:
    C_str = next(input_generator)
    C = int(C_str)
    
    for _ in range(C):
        N = int(next(input_generator))
        notas_list = []
        for _ in range(N):
            notas_list.append(int(next(input_generator)))
        
        # Converte para array C
        notas_array = (ctypes.c_int * N)(*notas_list)
        percentual = ctypes.c_double(0.0) # Alterado para double
        
        lib.calcular(N, notas_array, ctypes.byref(percentual))
        
        # Formata com 3 casas decimais 
        print(f"{percentual.value:.3f}%")

finally:
    if os.path.exists(tmp_c.name): os.unlink(tmp_c.name)
    if os.path.exists(tmp_so): os.unlink(tmp_so)