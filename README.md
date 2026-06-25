Установка:  
git clone https://github.com/TiRaN4eg/test_em  
cd ./test_em  
Оредактируйте файл .env, указав предпочтительные имена контейнеров  
docker-compose up -d  


Проверка работоспособности:  
curl http://localhost  
Ожидаемый ответ:  
"Hello from Effective Mobile!"  



Удаление:  
docker-compose down --rmi all