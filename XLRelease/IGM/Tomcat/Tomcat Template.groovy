// Exported from:        http://DESKTOP-5M38RP9:25516/#/templates/Foldera94108a908a140c59f61e244c7967f51-Foldera4db23785203402a889e9fd6aff06713-Releasedaf0d81b1fc64ee182ad79909cd4b970/releasefile
// XL Release version:   8.6.1
// Date created:         Thu Apr 25 11:08:53 EDT 2019

xlr {
  template('Tomcat Template') {
    folder('IGM/Tomcat')
    scheduledStartDate Date.parse("yyyy-MM-dd'T'HH:mm:ssZ", '2019-04-24T09:57:40-0400')
    dueDate Date.parse("yyyy-MM-dd'T'HH:mm:ssZ", '2019-04-24T10:57:40-0400')
    phases {
      phase('QA') {
        tasks {
          script('Deploy to Dev') {
            script (['''\
print ("Deploy WAR file to Tomcat")
'''])
          }
          custom('Run Jenkins Build') {
            description 'Run a Jenkins build pipeline'
            script {
              type 'jira.UpdateIssue'
              additionalFields 'one':'value-one'
            }
          }
          script('Specify Build Tag') {
            script (['''\
print ("Specify Build Tag")
'''])
          }
          script('Manual Smoke Tests') {
            description 'Manual Tasks'
            script (['''\
print ("Hello World")
'''])
          }
          script('Manual QM Regression Testing') {
            description 'Manual Tasks'
            script (['''\
print ("QM Regression Testing")
'''])
          }
          script('Manual Security Testing') {
            description 'Manual Tasks'
            script (['''\
print ("Security Testing")
'''])
          }
          script('Manual Performance Testing') {
            description 'Manual Tasks'
            script (['''\
print ("Performance Testing")
'''])
          }
        }
      }
      phase('DCES') {
        tasks {
          script('Gate:wait for approval from QA and Product Owner') {
            script (['''\
print ("Hello World")
'''])
          }
          script('Generate release notes') {
            description 'TOOD: JIRA integration to pull the notes.'
            script (['''\
print ("Hello World")
'''])
          }
          sequentialGroup('Deploy Tomcat (WAR) to Test') {
            tasks {
              script('Stop site') {
                script (['''\
print ("Stop Tomcat")
'''])
              }
              script('Deploy to Test') {
                description 'TODO: Deploy using XL Deply'
                script (['''\
print ("Deploy to Tomcat using XL Deploy")
'''])
              }
              script('Start site') {
                script (['''\
print ("Start Tomcat")
'''])
              }
            }
          }
          script('Run smoke tests on UI test agent') {
            script (['''\
print ("Hello World")
'''])
          }
          script('Gate:Fail release if smoke tests fail') {
            script (['''\
print ("Hello World")
'''])
          }
          script('Gate:Product Owner Approval') {
            description 'Different approvers (managers, director, product owner?) approve via email'
            script (['''\
print ("Hello World")
'''])
          }
          script('Submit ServiceNow change ticket (to test ServiceNow env for POC)') {
            description 'TODO: Need to integrate SNOW here.'
            script (['''\
print ("Hello World")
'''])
          }
        }
      }
      phase('ADP') {
        tasks {
          script('Gate:Wait for ServiceNow approval & window') {
            script (['''\
print ("Hello World")
'''])
          }
          script('Deploy to UAT/Test') {
            description 'TODO: Configure XLD for a rolling deployment.'
            script (['''\
print ("Rolling deployment to Tomcat.  Use XL Deploy")
'''])
          }
          script('Run smoke tests on UI test agent') {
            script (['''\
print ("Hello World")
'''])
          }
          script('Gate:deployment coodinator (from ServiceNow)') {
            description 'TODO: Product Owner Approval from ServiceNow'
            script (['''\
print ("Hello World")
'''])
          }
        }
      }
    }
    extensions {
      dashboard('Dashboard') {
        parentId 'Applications/Foldera94108a908a140c59f61e244c7967f51/Foldera4db23785203402a889e9fd6aff06713/Releasedaf0d81b1fc64ee182ad79909cd4b970'
        owner 'admin'
        tiles {
          releaseProgressTile('Release progress') {
            
          }
          releaseHealthTile('Release health') {
            
          }
          releaseSummaryTile('Release summary') {
            
          }
          resourceUsageTile('Resource usage') {
            
          }
          timelineTile('Release timeline') {
            
          }
        }
      }
    }
    
  }
}