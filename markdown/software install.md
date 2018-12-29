### 1.java
tar -zxvf jdk.tar.gz -C /usr/jdk
/etc/profile
```
export JAVA_HOME=/usr/jdk/jdk1.8.0_144
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
```
