# BBB-meetings-json
## Export BigBlueButton running meetings details to JSON.

### Usage

Add your API Url and SECRET KEY in docker-compose.yml file.  

<br /><br />
#### docker-compose:
```yaml
version: '3' 
services: 
  bbb-meetings-json:
    container_name: "bbb-meetings-json"
    image: mohammad362/bbb-meetings-json:1.0
    ports:
      - "8000:8000"
    environment:
      - API_URL=
      - API_SECRET_KEY=
    restart: unless-stopped
```
<br /><br />
visit http://server_ip:8000
