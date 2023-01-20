### Build Docker Image & Run Container
* PyCron-Upload
```
cd PyCron-Upload
docker build -t cron-upload .
docker run -it --rm --name cron-upload cron-upload
```
* PyCron-Run
```
cd PyCron-Run
docker build -t cron-run .
docker run -it --rm --name cron-run cron-run
```
* PyCron-test-db
```
cd PyCron-test-db
docker build -t cron-db .
docker run -it --rm --name cron-db cron-db
```
* PyCron-test-db2
```
cd PyCron-test-db2
docker build -t cron-db2 .
docker run -it --rm --name cron-db cron-db2
```
