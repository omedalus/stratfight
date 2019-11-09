#!/bin/bash

FUNCTION_NAME=$1

node -e "require(\"./$FUNCTION_NAME/index\").handler().then(x => console.log(x.body))" | jq