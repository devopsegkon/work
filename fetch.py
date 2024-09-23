import requests, yaml, sys, time

urls_status = {}

#Function that calculates UP outcomes and total requests.
def process_response(response, base_url):
    outcome_up = 0

    status_code = response.status_code

    elapsed_time_ms = (response.elapsed.total_seconds() * 1000)

    if (200 <= status_code <= 299) and (elapsed_time_ms < 500):
        outcome_up = 1

    if not base_url in urls_status:
        urls_status[base_url] = {}
        urls_status[base_url]["outcome_up"] = outcome_up
        urls_status[base_url]["total_requests"] = 1
    else:
        current_outcome_up = urls_status[base_url]["outcome_up"]
        urls_status[base_url]["outcome_up"] = current_outcome_up + outcome_up
        current_total_requests = urls_status[base_url]["total_requests"]
        urls_status[base_url]["total_requests"] = current_total_requests + 1

#Function needed to classify the outcome and total requests in the dictionary
def determine_base_url(url):
  split_by_double_slash = url.split("//")
  split_by_single_slash = split_by_double_slash[1].split("/")
  base_url = split_by_single_slash[0]
  return base_url


#Function that queries the URL according to the method, headers and body received.
def send_request(name, url, method, body, headers):
    r = ""
    if not method:
        method = "GET"

    if (headers and body):
        try:
            r = requests.request(method=method, url=url, headers=headers, data=body)
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
    elif headers:
        try:
            r = requests.request(method=method, url=url, headers=headers)
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
    elif body:
        try:
            r = requests.request(method=method, url=url, data=body)
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
    else:
        try:
            r = requests.request(method=method, url=url)
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

    base_url = determine_base_url(url)
    process_response(r, base_url)


#Function that will display the availability percentage according to what the
#dictionary urls_status has recorded so far.
def log_status(urls_status):
    for k,v in urls_status.items():
        outcome_up = v["outcome_up"]
        total_requests = v["total_requests"]

        percentage = round(100 * (outcome_up/total_requests))

        print(k + " has " + str(percentage) + "% " + "availability percentage")


#Function that takes an endpoint element from the yaml file and 
#extracts the needed arguments to send the request required per the method
def process_elem(http_endpoint_elem):
  name = http_endpoint_elem['name']
  url = http_endpoint_elem['url']
  
  method=""
  body=""
  headers=""
  if 'method' in http_endpoint_elem:
    method = http_endpoint_elem['method']
  if 'body' in http_endpoint_elem:
    body = http_endpoint_elem['body']
  if 'headers' in http_endpoint_elem:
    headers = http_endpoint_elem['headers']

  send_request(name, url, method, body, headers)



if len(sys.argv) == 2:
    param_file = sys.argv[1]
    fetch_urls_dict = ""
    #Open the yaml file passed as parameter
    try:
        f = open(param_file)
    except FileNotFoundError:
        print('File not found')
        sys.exit()
    else:
        with f as file:
            fetch_urls_dict = yaml.safe_load(file)
    #The script checks the URLs in the yaml file every 15 seconds
    while True:    

        for http_endpoint_elem in fetch_urls_dict:
            process_elem(http_endpoint_elem)

        log_status(urls_status)
        time.sleep(15)
elif len(sys.argv) > 2:
    print("Too many arguments. Pass only the path to the yaml file.")
else:
    print("Need the full path to the yaml file.")