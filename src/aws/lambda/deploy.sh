#!/bin/bash

deploy_lambda_function() {
  FUNCTION_NAME=$1
  LAMBDA_NAME="StratFight_$FUNCTION_NAME"
  ZIPFILE_NAME="$FUNCTION_NAME.zip"

  cd "$FUNCTION_NAME"
  zip -r "$ZIPFILE_NAME" *

  aws lambda update-function-code \
      --function-name "$LAMBDA_NAME" \
      --zip-file "fileb://$ZIPFILE_NAME"

  rm "$ZIPFILE_NAME"
}

FUNCTION_NAME=$1

if [ -z "$FUNCTION_NAME" ]; then
  for FUNCTION_NAME in `ls -d */ | cut -f1 -d'/'`; do
    deploy_lambda_function "$FUNCTION_NAME"
  done
else
  deploy_lambda_function "$FUNCTION_NAME"
fi


