mkdir package  
pip install --target ./package requests 
cd package   
zip -r ../my_deployment_package.zip .  
cd .. 
touch lambda_function.py  
zip my_deployment_package.zip lambda_function.py
chmod 755 my_deployment_package.zip
aws lambda update-function-code --function-name callEC2 --zip-file fileb://my_deployment_package.zip