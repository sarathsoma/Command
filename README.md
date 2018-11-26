# Command
A boilerpate project to create unix like commands using [Click](https://github.com/pallets/click).

Steps to create a command :

1.	Clone the repository
	`
	git clone https://github.com/sarathsoma/Command.git
	`
2. Install dependencies
	`
	pip install -r requirements.txt
	`
	
3. Create a module / command using click
4. Link your command in `setup.py` in `entry_points` section.
5. Use `pip install .` to install your command locally. This will create a binary of your command in your local environment. 
6. Happy Coding!
