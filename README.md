# NativeCpp_Electron_GUI

NOTE IT DOESN'T WORK YET!!!


I do not recommend using this code yet I am just trying to get native c++ running on my GUI using electron.

check version

npm -v
5.6.0
node -v
v9.3.0

commands used:

mkdir electroncpp	//or whatever
cd electroncpp		//or whatever

npm init -y		//node package manager initialize and skip output
			//creates package.json
sudo npm install -g electron node-gyp --unsafe-perm=true --allow-root --save-dev --save-exact

change line
	"main": "index.js",
to
	"main": "bindings.js"
this is for the bindings

	"test": "echo \"Error: no test specified\" && exit 1"
to
	"start": "electron ."
this will launch the application when we type npm start

now we need main.js for electron to actually start
so at https://electronjs.org/docs/tutorial/quick-start
scroll down a bit and there is the main.js file wich you can just copy paste and make main.js
