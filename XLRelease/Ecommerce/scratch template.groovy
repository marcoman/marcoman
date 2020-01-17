// Exported from:        http://DESKTOP-5M38RP9:25516/#/templates/Folderd0cb4af40e01407e9094000f2cf45db2-Release5c3b42ecc209440caec1c4c242caaa1e/releasefile
// XL Release version:   9.5.2
// Date created:         Thu Jan 16 16:59:15 EST 2020

xlr {
  template('scratch template') {
    folder('Ecommerce')
    variables {
      stringVariable('buildNumber') {
        required false
        showOnReleaseStart false
      }
      stringVariable('ticket') {
        required false
        showOnReleaseStart false
      }
      stringVariable('changeRequestId') {
        required false
        showOnReleaseStart false
      }
      stringVariable('changeRequestSysId') {
        required false
        showOnReleaseStart false
      }
      stringVariable('changeRequestStatus') {
        required false
        showOnReleaseStart false
      }
      stringVariable('jiraticket') {
        required false
        showOnReleaseStart false
      }
      stringVariable('applicationVersionInProd') {
        required false
        showOnReleaseStart false
      }
      booleanVariable('monitorResult') {
        required false
        showOnReleaseStart false
      }
      stringVariable('memoryDEV') {
        required false
        showOnReleaseStart false
        label 'DEV Memory'
        description 'Memory for DEV MarkLogic'
        value '16 GB'
      }
      stringVariable('memoryUAT') {
        required false
        showOnReleaseStart false
        label 'UAT Memory'
        description 'Memory for UAT MarkLogic'
        value '256 GB'
      }
      stringVariable('memoryPROD') {
        required false
        showOnReleaseStart false
        label 'PROD Memory'
        description 'Memory for PROD MarkLogic'
        value '256 GB'
      }
      integerVariable('coresDEV') {
        required false
        showOnReleaseStart false
        label 'DEV Cores'
        description 'Cores for DEV MarkLogic'
        value 8
      }
      integerVariable('coresUAT') {
        required false
        showOnReleaseStart false
        label 'UAT Cores'
        description 'Cores for UAT MarkLogic'
        value 64
      }
      integerVariable('coresPROD') {
        required false
        showOnReleaseStart false
        label 'PROD Cores'
        description 'Cores for PROD MarkLogic'
        value 64
      }
      stringVariable('enviro') {
        required false
        showOnReleaseStart false
        value 'TEST'
      }
    }
    scheduledStartDate Date.parse("yyyy-MM-dd'T'HH:mm:ssZ", '2016-02-02T03:00:00-0500')
    dueDate Date.parse("yyyy-MM-dd'T'HH:mm:ssZ", '2019-07-26T09:17:20-0400')
    tags 'ecommerce', 'java'
    scriptUsername 'admin'
    scriptUserPassword '{aes:v0}rSGizEpt2o9P+9W7+5clrUI3UkksM5uIDiUKrQdDlZc='
    phases {
      phase('PLAN') {
        color '#009CDB'
        tasks {
          custom('Create Change Request-update') {
            script {
              type 'servicenow.CreateRequestItem'
              servicenowServer 'Ecommerce'
              shortDescription 'PetPortal Demo'
              sysId variable('changeRequestSysId')
              'Ticket' variable('changeRequestId')
            }
          }
          custom('Create User Story-track') {
            description 'This user story is for design of the microsite feature on the\n' +
                        'ecommerce website. This is in relation to ${changeRequestId}'
            script {
              type 'jira.CreateIssue'
              jiraServer 'Ecommerce'
              project 'SAN'
              title '${changeRequestId}: microsite feature on the ecommerce website'
              description 'This user story is for design of the microsite feature on the\n' +
                          '  ecommerce website. This is in relation to ${changeRequestId}'
              issueId variable('jiraticket')
            }
          }
          custom('Notify on Slack') {
            script {
              type 'slack.Notification'
              server 'Ecommerce'
              channel '#mmorales'
              message 'Created change request ${changeRequestId} and user story ${jiraticket} for development'
            }
          }
          manual('User story and change request review') {
            owner 'David'
            tags 'approval'
          }
        }
      }
      phase('DEV') {
        color '#009CDB'
        tasks {
          custom('Build package') {
            script {
              type 'jenkins.Build'
              jenkinsServer 'Ecommerce'
              jobName 'petclinic-artifactory'
              buildNumber variable('buildNumber')
            }
          }
          custom('Code Quality Analysis') {
            script {
              type 'sonar.checkCompliance'
              sonarServer 'Ecommerce'
              resource 'org.springframework.samples:spring-petclinic'
            }
          }
          custom('Secure Code Analysis') {
            taskRecoverOp com.xebialabs.xlrelease.domain.recover.TaskRecoverOp.RUN_SCRIPT
            script {
              type 'fortify.checkCompliance'
              fortifyServer 'Ecommerce'
              projectName 'Address Book'
              projectVersion 'COOL-234'
              minimumStarRating 2
            }
          }
          custom('Deploy to DEV') {
            script {
              type 'xldeploy.Deploy'
              server 'Ecommerce'
              retryCounter 'currentContinueRetrial':'0','currentPollingTrial':'0'
              deploymentPackage 'petclinic-artifactory/1.0.${buildNumber}'
              deploymentEnvironment 'Environments/Dev/TEST'
            }
          }
          script('Automated system testing') {
            owner 'admin'
            script (['''\
import time
time.sleep(5)
print "Performing Smoke Tests"
'''])
          }
          custom('Update User Story') {
            script {
              type 'jira.UpdateIssue'
              jiraServer 'Ecommerce'
              issueId '${jiraticket}'
              newStatus 'IN PROGRESS'
              comment 'Deployed to DEV'
            }
          }
          custom('Update change request') {
            script {
              type 'servicenow.UpdateRequestItem'
              servicenowServer 'Ecommerce'
              sysId '${changeRequestSysId}'
            }
          }
          gate('QA Control Approval') {
            owner 'admin'
            tags 'approval'
            conditions {
              condition('Automated System testing successful ?')
              condition('Unit testing successful ?')
              condition('All manual test cases prepared and verified ?')
              condition('Code quality and security analysis desirable ?')
            }
          }
          custom('Notify on Slack') {
            script {
              type 'slack.Notification'
              server 'Ecommerce'
              channel '#mmorales'
              message 'Application deployed successfully to DEV environment'
            }
          }
        }
      }
      phase('DEPLOY TO INACTIVE') {
        color '#009CDB'
        tasks {
          custom('Deploy to INACTIVE') {
            script {
              type 'xldeploy.Deploy'
              server 'Ecommerce'
              retryCounter 'currentContinueRetrial':'0','currentPollingTrial':'0'
              deploymentApplication 'Applications/petclinic-artifactory'
              deploymentVersion '1.0.1'
              deploymentPackage 'Applications/petclinic-artifactory/1.0.1'
              deploymentEnvironment 'Environments/Dev/${enviro}'
            }
          }
          script('Load Testing') {
            owner 'admin'
            script (['''\
import time
time.sleep(10)
print "Performing  Load Tests"
'''])
          }
          parallelGroup('Perform Automated Testing') {
            tasks {
              script('Smoke tests') {
                owner 'admin'
                script (['''\
import time
time.sleep(20)
print "Performing Smoke Tests"
'''])
              }
              script('API Testing') {
                owner 'admin'
                script (['''\
import time
time.sleep(5)
print "Performing Smoke Tests"
'''])
              }
            }
          }
          custom('Vulnerability Scan') {
            script {
              type 'fortify.checkCompliance'
              fortifyServer 'Ecommerce'
              projectName 'Address Book'
              projectVersion 'COOL-234'
              minimumStarRating 1
            }
          }
          custom('Update User Story') {
            script {
              type 'jira.UpdateIssue'
              jiraServer 'Ecommerce'
              issueId '${jiraticket}'
              comment 'Deployed to QA'
            }
          }
          custom('Update change request') {
            script {
              type 'servicenow.UpdateRequestItem'
              servicenowServer 'Ecommerce'
              sysId '${changeRequestSysId}'
            }
          }
          gate('QA Control Approval') {
            owner 'admin'
            tags 'approval'
            conditions {
              condition('Load testing successful ?')
              condition('Vulnerability scan results acceptable ?')
              condition('Smoke testing successful ?')
            }
          }
          custom('Notify on Slack') {
            script {
              type 'slack.Notification'
              server 'Ecommerce'
              channel '#mmorales'
              message 'Application deployed successfully to TEST environment'
            }
          }
        }
      }
      phase('PROD') {
        color '#009CDB'
        tasks {
          custom('Get Current Application Version in Production') {
            script {
              type 'xld.GetLastVersionDeployed'
              server 'Ecommerce'
              environmentId 'Environments/Dev/TEST'
              applicationName 'petclinic-artifactory'
              applicationId variable('applicationVersionInProd')
            }
          }
          custom('Switch over PROD') {
            script {
              type 'xldeploy.Deploy'
              server 'Ecommerce'
              retryCounter 'currentContinueRetrial':'0','currentPollingTrial':'0'
              deploymentPackage 'petclinic-artifactory/1.0.${buildNumber}'
              deploymentEnvironment 'Environments/Dev/${enviro}'
            }
          }
          gate('Verify PROD Deployment') {
            owner 'admin'
            tags 'approval'
            conditions {
              condition('Smoke Tests Successful')
              condition('Test Transaction Successful')
            }
          }
          custom('Close change request') {
            script {
              type 'servicenow.UpdateRequestItem'
              servicenowServer 'Ecommerce'
              sysId '${changeRequestSysId}'
            }
          }
          custom('Update User Story') {
            script {
              type 'jira.UpdateIssue'
              jiraServer 'Ecommerce'
              issueId '${jiraticket}'
              comment 'Deployed to QA'
            }
          }
          custom('Notify on Slack') {
            script {
              type 'slack.Notification'
              server 'Ecommerce'
              channel '#mmorales'
              message 'Application deployed successfully to PROD environment'
            }
          }
        }
      }
      phase('OPERATION') {
        color '#0099CC'
        tasks {
          script('Application checks') {
            owner 'admin'
            script (['''\
import time
import random
time.sleep(10)
print "Performing  Load Tests"
if random.randint(0, 1) < 1:
    releaseVariables['monitorResult'] = False
else:
    releaseVariables['monitorResult'] = True
'''])
          }
          parallelGroup('Monitoring Actions') {
            tasks {
              sequentialGroup('Rollback Activities') {
                tasks {
                  custom('Rollback - If Failure') {
                    precondition '${monitorResult}'
                    script {
                      type 'xldeploy.Deploy'
                      server 'Ecommerce'
                      retryCounter 'currentContinueRetrial':'0','currentPollingTrial':'0'
                      deploymentPackage '${applicationVersionInProd}'
                      deploymentEnvironment 'Environments/Dev/TEST'
                    }
                  }
                  custom('Failure Notification') {
                    precondition '${monitorResult}'
                    script {
                      type 'slack.Notification'
                      server 'Ecommerce'
                      channel '#mmorales'
                      message 'The Production Deployment for App petclinic-artifactory/1.0.${buildNumber} failed and has been rolled back to the previous version : ${applicationVersionInProd}'
                    }
                  }
                }
              }
              custom('Success Notification') {
                precondition 'not ${monitorResult}'
                script {
                  type 'slack.Notification'
                  server 'Ecommerce'
                  channel '#mmorales'
                  message 'The Production Deployment for App petclinic-artifactory/1.0.${buildNumber} has been successfully done.'
                }
              }
            }
          }
        }
      }
    }
    extensions {
      dashboard('Dashboard') {
        parentId 'Applications/Folderd0cb4af40e01407e9094000f2cf45db2/Release519bbaa1041c455ca5882b84515a2f4c'
        owner 'admin'
        tiles {
          releaseProgressTile('Release progress') {
            
          }
          releaseHealthTile('Release health') {
            
          }
          releaseSummaryTile('Release summary') {
            
          }
          resourceUsageTile('Resource usage') {
            width 1
            row 3
          }
          timelineTile('Release timeline') {
            height 1
            width 1
            row 2
          }
          serviceNowQueryTile('ServiceNow tickets') {
            row 1
            col 2
            servicenowServer 'Ecommerce'
            tableName 'incident'
            detailsViewColumns 'number':'number','short_description':'short_description','state':'state','priority':'priority','assigned_to':'assigned_to.display_value'
          }
          jiraQueryTile('JIRA issues') {
            row 1
            col 0
            jiraServer 'Ecommerce'
            query 'PROJECT = SAN and type = Task'
          }
          taskProgressTile('Task Progress') {
            row 1
            col 1
            tags 'approval'
          }
          deploymentsActivityTile('Deployment activity') {
            width 1
            row 2
            col 2
          }
          deploymentsDistributionTile('Deployments distribution') {
            row 2
            col 1
          }
        }
      }
    }
    
  }
}