# datascience-template @ ROCS
Template repository for datascience projects on Jupyterhub

## Getting Started:

### If you are using our Jupyterhub for the first time, follow these steps
* [ ] Create Github Account
* [ ] Setup HU VPN
	* [ ] Add Github Account to rocs-org
* [ ] Log in to Jupyterhub (https://ornt.biologie.hu-berlin.de/jupyterhub)
* [ ] Create ssh key and set ownership
	* [ ] Open a new terminal on Jupyterhub
	* [ ] run `ssh-keygen` and give your key a password
* [ ] Add ssh key to Github account
	* [ ] In your Jupyterhub terminal run `cat ~/.ssh/id_rsa.pub` and copy the output.
	* [ ] Go to https://github.com/settings/keys
	* [ ] click `New SSH key`, give your key a name and paste the output from above.

### If you are starting a new project, skip until here
* [ ] Clone example repository and install dependencies
	* [ ] Go to https://github.com/rocs-org/datascience-template
	* [ ] Click `Use this template` and fill in the required fields
	* [ ] In your new repo, click on `Code`, copy the ssh url and in your Jupyter console run `git clone <your repo url>`
	* [ ] If git complains about permissions of your ssh key, run `chmod 600 ~/.ssh/id_rsa` and try again.
	* [ ] Enter the new folder and run
		* [ ] `make install`
		* [ ] `make install-kernel name=<some name you like>`
		* [ ] Restart your server to make the kernel available (File -> Hub Control Panel -> Stop My Server -> Start My Server)
	* [ ] Then open the example notebook and select your new kernel.
	* [ ] Open https://rocs-dbt-docs.netlify.app to get an overview of the available raw and preprocessed data.
