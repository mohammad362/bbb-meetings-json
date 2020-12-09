# First Release

## Export BigBlueButton running meetings details to JSON.

### Usage

Create "config.env" file and fill required fields.  

Ex:  
```
API_URL = 'https://example.com/bigbluebutton/api/'  
API_SECRET_KEY = '123456789abcdef'  
```
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
    volumes:
      - ./config.env:/app/config.env
    restart: unless-stopped
```
<br /><br />
visit http://server_ip:8000
