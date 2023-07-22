#------------ ID's and Service Accounts of Projects
# Modify the values according to your Google Cloud account

Project_0_ID = 'project_0'
Project_1_ID = 'project_1'
Project_2_ID = 'project_2'
Project_3_ID = 'project_3'
Project_4_ID = 'project_4'

Account_0 = 'account_0@developer.gserviceaccount.com'
Account_1 = 'account_1@developer.gserviceaccount.com'
Account_2 = 'account_2@developer.gserviceaccount.com'
Account_3 = 'account_3@developer.gserviceaccount.com'
Account_4 = 'account_4@developer.gserviceaccount.com'

Project_0 = [Project_0_ID, Account_0, 'Project_0']
Project_1 = [Project_1_ID, Account_1, 'Project_1']
Project_2 = [Project_2_ID, Account_2, 'Project_2']
Project_3 = [Project_3_ID, Account_3, 'Project_3']
Project_4 = [Project_4_ID, Account_4, 'Project_4']

Project_list = [Project_0, Project_1, Project_2, Project_3, Project_4]

#------------ Regions and MV's Configs
# Check the limits of your Google Cloud account as well as the best zones for your project

Zone_1 = 'us-west4-b'
Zone_2 = 'us-west3-b'
Zone_3 = 'us-west2-b'
Zone_4 = 'us-west1-b'
Zone_5 = 'us-east5-a'

MV_per_zone = 3

Zone_list = [Zone_1, Zone_2, Zone_3, Zone_4, Zone_5]

SSD_size = "160"

#------------ Start Download
# Where to resume the download if it's partially completed

Start = 0

#------------ MV's creation

for Project in Project_list:
   file = open(Project[2] + '_Create_MV.txt', 'w')

   MV_id = 1

   for zone in Zone_list:
       for i in range(MV_per_zone):

           file.write('gcloud compute instances create mv-' + str(MV_id) + ' --project=' + Project[0] + ' --zone=' + zone
                      + ' --machine-type=n2d-highcpu-2 --network-interface=network-tier=PREMIUM,subnet=default --ma'
                      + 'intenance-policy=MIGRATE --provisioning-model=STANDARD --service-account=' + Project[1]
                      + ' --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/au'
                      + 'th/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/'
                      + 'auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.go'
                      + 'ogleapis.com/auth/trace.append --tags=http-server,https-server --create-disk=auto-delete=yes,bo'
                      + 'ot=yes,device-name=mv-' + str(MV_id) + ',image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v2'
                      + '0220905,mode=rw,size=' + SSD_size + ',type=projects/teste-363902/zones/' + zone + '/diskTypes/pd-ssd --no-shiel'
                      + 'ded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any\n')
           MV_id += 1
   file.close()

#------------ Create Upload & Download

for Project in Project_list:
    file = open(Project[2] + '_Upload.txt', 'w')
    file2 = open(Project[2] + '_Download.txt', 'w')

    MV_id = 1

    for zone in Zone_list:
        for i in range(MV_per_zone):

            file.write('gcloud compute scp --project="' + Project[0] + '" --zone="' + zone + '" ~/Upload/find_prime_palindrome ~/Upload/'
                  + str(Start) + '/1.sh mv-' + str(MV_id) + ':~/\n')
            
            file2.write('gcloud compute scp --project="' + Project[0] + '" --zone="' + zone + '" --recurse mv-'
                        + str(MV_id) + ':~/real/' + str(Start) + '/' + str(Start) + ' ~/Download\n')

            MV_id += 1
            Start += 1
    file.close()
    file2.close()
    
#------------ Create Initiator

file = open('Initiator.txt', 'w')

MV_id = 1

for zone in Zone_list:
    for i in range(MV_per_zone):
        file.write('nohup gcloud compute ssh mv-' + str(MV_id) + ' --zone=' + zone + ' --command="sed -i \'s/\\r//\' 1.sh && chmod u+r+x 1.sh &&'
                   + ' nohup ./1.sh >> admin.log" &\n')
        MV_id += 1
file.close()
