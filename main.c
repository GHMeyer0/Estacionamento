#include <stdio.h>
#include <stdlib.h>
#include <time.h>  
#include <sys/types.h>
#include <pthread.h>
#include <semaphore.h>

typedef struct
{
    int numero;
    sem_t disponivel;
} Vagas;

Vagas _vaga[];

int main() {
    CriarVagas(10);
    for (size_t i = 0; i < 10; i++)
    {
        printf("O Numero é %d \n", _vaga[i].numero);
       sem_wait(&_vaga[i].disponivel);
       sem_post(&_vaga[i].disponivel);
       if( sem_trywait(&_vaga[i].disponivel)){
           printf("TRUE");
       } else
       {
           printf("FALSE");
       }
    }
}



void CriarVagas(int quantidade_de_vagas){
    for (int i = 0; i <= quantidade_de_vagas; i++)
    {
        _vaga[i].numero = i;
        sem_init(&_vaga[i].disponivel, 0, 1);
    }
}

void EntrarCarro(){
}

void SairCarro(){

}

