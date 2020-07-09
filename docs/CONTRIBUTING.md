# Contributing 

We are excited to have your innovative input to this project!

When contributing to this repository, please first discuss the change you wish to make via an issue, email, or any other method with the maintainers of this repository
before making a change.

See a summary of instructions to guide how you can contribute.

    1. Fork the Project repo 
    2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
    3. Commit your Changes (git commit -m 'Add some AmazingFeature')
    4. Push to the Branch (git push origin feature/AmazingFeature)
    5. Open a Pull Request
    6. You can also get in touch via email landrs@nd.edu or visit https://www.landrs.org/
    
# Example of contributing to the LANDRS PySOSA project

Step 1. Set up a working copy of the pysosa project on your computer

        $ git clone https://github.com/landrs-toolkit/PySOSA.git
             
   Then change into the new project repository
             
         $ cd <some_path>/PySOSA
         
   Set up a new remote that points to the original project so that you can grab any changes and bring them into your local copy.

          $ git remote add upstream https://github.com/landrs-toolkit/PySOSA.git
 

Step 2. Get it working on your machine. 
    Now that you have the source code, get it working on your computer. There is documentation on how to do this in the README file. 

Step 3. Do some work
    
This is the fun bit where you get to contribute to the project. Pick an issue, reproduce it on your version. Once you have reproduced it, read the code to work out where the problem is. 
Once you’ve found the code problem, you can move on to fixing it.

Branch!

The number one rule is to put each piece of work on its own branch. If you are bug fixing, then branch from master
and if you are adding a new feature then branch from develop. For this example, we’ll assume we’re fixing a bug 
in PySOSA, so we branch from master:
         
        $ git checkout master
        $ git pull upstream master && git push origin master
        $ git checkout -b hotfix/PySOSA-readme-update
        
        Now do the work to fix the issue
        
        
Step 4. Create the Pull Request

To create a PR you need to push your branch to the origin remote and then press compare and pull request buttons on GitHub.

To push a new branch:
*       $ git push -u origin hotfix/PySOSA-readme-update

This will create the branch on your GitHub project. The -u flag links this branch with the remote one, so that in the future, you can simply type git push origin.

Open a Pull Request

    Click compare and pull request button to open the PR. Click the link which will take you to the project’s CONTRIBUTING file and read it! It contains valuable information on how to work with the project’s code base and will help you get your contribution accepted.

Step 5. Review by the maintainers

For your work to be integrated into the project, the maintainers will review your work and either request changes or merge it.


 # Pull Request Process
 
    * Ensure any install or build dependencies when doing a build are documented.
    * Update the README.md with details of changes to the modules and or interfaces, this includes new environment variables, exposed ports, useful file locations and container parameters.
    * Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent. 
    * You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

 
 
# Desired TODOs
some ideas on what you can extend on: 
- PySOSA Demo
- Example to  Query the pysosa graphs
- test sampler, procedure and actuator adding 
- show all sensors on a particular platform, list all their observations, simulate them etc.



# Conduct
* Discuss with us the desired changes on the project [landrs website](https://www.landrs.org/)
* Email us at landrs@nd.edu
* Please note we have a code of conduct to be followed in all interactions with the project i.e. discuss first with project maintainers when you suggest a change.





