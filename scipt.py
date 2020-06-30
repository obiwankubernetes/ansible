### Creating and Using VM

# 1. Go to Azure Portal
# 2. Go to Azure Cloud Shell
# 3. go into Cloud drive -> cd clouddrive
# 4. make new dir -> mkdir <name>
# 5. switch into the new dir -> cd <name>
# 6. create new yml file for anible playbook in Azure Cloud Shell code editor -> code <name>.yml
# 7. save .yml file (ctrl+S) and exit editor (ctrl+
# 8. run ansible playbook to provision resources -> ansible-playbook <name>.yml
# 9. ensure resources created -> check portal
# 10. get into vm -> ssh azureuser@<given_public_ip_address>

### Managing VM

# stop vm

# 11. create stop-vm.yml playbook
# 12. activate stop playbook -> ansible-playbook vm-stop.yml

# start vm

# 13. create start vm.yml
# 14. init start playbook -> ansible-playbook vm-start.yml