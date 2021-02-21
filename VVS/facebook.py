import facebook

def main():
   # Fill in the values noted in previous steps here
   cfg = {
   "page_id"      : "1xxxxx48480xxxx",  # Step 1
   "access_token" : "EAANO6Hx2hlkBAG90KYZAV6EpdfhsYg6FWbiL35qvXAio0R7ZC1a0b37nrMZBLKNHRFL4my2lgJVMO5NaWrgv1RPZAtHKp8Mtx93XoJZB0fZCJZCX6yNsbU9pf6cLCQ0G6fFZAi4lUjYF5OugjZAP8W8aWO4GFHZAry0ZACsCeUpc24SMWAvJoUwnDMsZCLu6HtD8yrQZBXgzyn4oHrfWOur00zgkw9XluIePbZCCOljM6QDbZBsfQZDZD"   # Step 3
    }

    api = get_api(cfg)
    msg = "Hello, world!"
    status = api.put_wall_post(msg)

def get_api(cfg):

    graph = facebook.GraphAPI(cfg['access_token'])
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
    if page['id'] == cfg['page_id']:
        page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)
    return graph

if __name__ == "__main__":
 main()