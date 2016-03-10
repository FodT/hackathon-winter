DEPLOYDIR=lambda-deploy

all: config build bundle 

clean:
	@rm -f config
	@rm -rf $(DEPLOYDIR)

config: 
	@echo "[prod]" >> config
	@echo "user=$(T1_PARTNER_USERNAME)" >> config
	@echo "pass=$(T1_PARTNER_PASSWORD)" >> config
	@echo "api_key=$(T1_PARTNER_API_KEY_PROD)" >> config
	@echo "api_url=t1.mediamath.com" >> config
	@echo "[sandbox]" >> config
	@echo "user=$(T1_PARTNER_USERNAME)" >> config
	@echo "pass=$(T1_PARTNER_PASSWORD)" >> config
	@echo "api_key=$(T1SANDBOX_API_KEY)" >> config
	@echo "api_url=t1sandbox.mediamath.com" >> config

build:
	@mkdir $(DEPLOYDIR)
	@cp sync_users.py $(DEPLOYDIR)
	@mv config $(DEPLOYDIR)
	@pip install terminalone -t $(DEPLOYDIR)
	@pip install future -t $(DEPLOYDIR)

bundle: 
	@cd $(DEPLOYDIR) && zip -r ../deploy .
	@rm -rf $(DEPLOYDIR)