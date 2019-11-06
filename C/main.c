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

Vagas vagas[];

int main() {
    
    CriarVagas(10);
    
    for (size_t i = 0; i < 10; i++)
    {
        printf("O Numero é %d \n", vagas[i].numero);
       sem_wait(&vagas[i].disponivel);
       sem_post(&vagas[i].disponivel);
       if( sem_trywait(&vagas[i].disponivel)){
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
        vagas[i].numero = i + 1;
        sem_init(&vagas[i].disponivel, 0, 1);
    }
}

void EntrarCarro(){
    for (size_t i = 0; i < 10; i++)
    {
       if (vagas[i].disponivel)
       {
           /* code */
       }
       
    }
    
}

void SairCarro(){

}

