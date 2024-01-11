python run.py --enc_in 7 --dec_in 7 --c_out 7 --use_weights 1
python run.py --enc_in 7 --dec_in 7 --c_out 7 --use_weights 0

python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 1 --future 0 --external_var temp 
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 0 --future 0 --external_var temp
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 1 --future 1 --external_var temp 
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 0 --future 1 --external_var temp

python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 1 --future 0 --external_var humidity 
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 0 --future 0 --external_var humidity
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 1 --future 1 --external_var humidity 
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 0 --future 1 --external_var humidity

python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 1 --future 0 --external_var wind_speed 
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 0 --future 0 --external_var wind_speed
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 1 --future 1 --external_var wind_speed 
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 0 --future 1 --external_var wind_speed

python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 1 --future 0 --external_var rain_1h 
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 0 --future 0 --external_var rain_1h
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 1 --future 1 --external_var rain_1h 
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 0 --future 1 --external_var rain_1h

python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 1 --future 0 --external_var clouds_all 
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 0 --future 0 --external_var clouds_all
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 1 --future 1 --external_var clouds_all 
python run.py --enc_in 8 --dec_in 8 --c_out 8 --use_weights 0 --future 1 --external_var clouds_all

python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 1 --future 0 --external_var wind_speed humidity rain_1h clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 0 --future 0 --external_var wind_speed humidity rain_1h clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 1 --future 1 --external_var wind_speed humidity rain_1h clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 0 --future 1 --external_var wind_speed humidity rain_1h clouds_all

python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 1 --future 0 --external_var temp humidity rain_1h clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 0 --future 0 --external_var temp humidity rain_1h clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 1 --future 1 --external_var temp humidity rain_1h clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 0 --future 1 --external_var temp humidity rain_1h clouds_all

python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 1 --future 0 --external_var temp wind_speed rain_1h clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 0 --future 0 --external_var temp wind_speed rain_1h clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 1 --future 1 --external_var temp wind_speed rain_1h clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 0 --future 1 --external_var temp wind_speed rain_1h clouds_all

python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 1 --future 0 --external_var temp wind_speed humidity clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 0 --future 0 --external_var temp wind_speed humidity clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 1 --future 1 --external_var temp wind_speed humidity clouds_all
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 0 --future 1 --external_var temp wind_speed humidity clouds_all

python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 1 --future 0 --external_var temp wind_speed humidity rain_1h
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 0 --future 0 --external_var temp wind_speed humidity rain_1h
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 1 --future 1 --external_var temp wind_speed humidity rain_1h
python run.py --enc_in 11 --dec_in 11 --c_out 11 --use_weights 0 --future 1 --external_var temp wind_speed humidity rain_1h

python run.py --enc_in 12 --dec_in 12 --c_out 12 --use_weights 1 --future 0 --external_var temp wind_speed humidity rain_1h clouds_all
python run.py --enc_in 12 --dec_in 12 --c_out 12 --use_weights 0 --future 0 --external_var temp wind_speed humidity rain_1h clouds_all
python run.py --enc_in 12 --dec_in 12 --c_out 12 --use_weights 1 --future 1 --external_var temp wind_speed humidity rain_1h clouds_all
python run.py --enc_in 12 --dec_in 12 --c_out 12 --use_weights 0 --future 1 --external_var temp wind_speed humidity rain_1h clouds_all