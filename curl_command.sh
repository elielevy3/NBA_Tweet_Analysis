Bearer=AAAAAAAAAAAAAAAAAAAAAPireAEAAAAASFiCUqL8SSaVtQ%2B3ofO2hW59sns%3D76UGPFvIlbtg2vBhDE2JdobdHKkE0TWP1jAItCfijJjqEMhS1s

# set up rules
#curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \
#-H "Content-type: application/json" \
#-H "Authorization: Bearer $Bearer" -d \
#'{
#  "add": [
#    { "value": "#LeBronJames Lebron"}
#  ]
#}'
# rule id =>


#curl -X POST 'https://api.twitter.com/2/tweets/search/all' \
#  -H "Content-type: application/json" \
#  -H "Authorization: Bearer $Bearer" -d \
#  '{
#    "delete": {
#      "ids": [
#        "1541070828447698949"
#      ]
#    }
#  }'


#curl -X GET 'https://api.twitter.com/2/tweets/search/stream' -H "Content-type: application/json" -H "Authorization: Bearer $Bearer" \
#  '{
#      "ids": [
#        "1541067119802335237"
#      ]
#  }'

#curl --request GET 'https://api.twitter.com/2/tweets/search/all?query=(Lebron)&max_results=500' --header "Authorization: Bearer $Bearer"


curl --request GET 'https://api.twitter.com/2/tweets/search/recent?query=(Lebron)&max_results=50' --header "Authorization: Bearer $Bearer"

# launching GET Requests
#curl -X GET -H "Authorization: Bearer $Bearer" "https://api.twitter.com/2/tweets/search/stream"