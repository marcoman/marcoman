# xlr-user-count-plugin
Count the number of users in XLD or XLD

## Build

After `./gradlew assemble` plugin jar can be found in the `build/libs/` directory. 

## Release

Make sure you have committed all files.

Release an alpha with this command

    gradle clean build release -Prelease.scope=patch -Prelease.stage=alpha

