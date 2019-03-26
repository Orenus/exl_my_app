
docker run \
-e CONF_FILE='/mnt/data/exl_my_app/config/app.properties' \
-e EXL_TRACE='1' \
-v /Users/orenus/Documents/dev/exl/project1:/mnt/data \
-i exl_py  python ./my_app.py -t 10