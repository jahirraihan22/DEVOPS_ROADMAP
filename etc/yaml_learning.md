<!-- @format -->

# YAML 101

## Introduction

**YAML** is a data serialization language. It is one of the most formatting languages display data in a non-human readable format. It become more popular than XML or JSON because of it's readability and it represents way more easier than those languages. It is nearly human readable language. The acronym was later changed to **"YAML Ain’t Markup Language”**  to emphasize that the language is intended for data and not documents. **YAML** is a common option when it comes to writing configuration files for Infrastructure as a Code (IaC). This files are used to store parameters and settings for desired cloud environment. Many Configuration management tools are using **YAML**. It is more secure when it comes to exchange files with third parties because it has no executable commands. It's file extension is *.yml*

## Basic Syntax

```yaml
microservice:
  app: user-authentication
  port: 9000
  version: 1.0
```

***Note:*** microservice is an object  

## String

***Note:***

- " ", ' ' or without quote
- app: "user-authentication"
- app: 'user-authentication'

## Multi-line Strings

``` yaml

multilineStringAsMultiline: |
  this is multiline string
  this is next line
  this is next line

multilineStringAsSingleLine: >
  this is a single line string,
  this should be in the same line.
  some other stuff
```

Examples:

``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
    name: mosquitto-config-file
data:
mosquitto.conf: |
    log_dest stdout
    log_type all
    log_timestamp true
    listener 9001
```

``` yaml
command: >
echo "this is very 
large 
sentence"
    
```

***Note:***

- (|) operator will interpret the string as multiple line
- (>) operator will interpret the string as single line

## List

```yaml
microservice:
  - app: user-authentication
    port: 9000
    version: 1.0
```

## Multiple List

``` yaml

microservices: 
  - app: user-authentication
    port: 9000
    version: 1.0
    deployed: yes
  - app: shopping-cart
    port: 9001
    versions: 
      - 1.9
      - 1.2
      - 1.6
  - app: admin-panel
    port: 9003
    versions: [1.8, 1.7, 1.5]
  
```

***Note:*** we can use multiple list using (-) also we can use it as an array

## Boolean

```yaml
microservice:
  - app: user-authentication
    port: 9000
    version: 1.0
    deployed: yes
    # deployed: true
    # deployed: on
    # deployed: off
```

***Note:*** for boolean there multiple are supported keywords like yes/no , true/false, on/off

## Environment Variables

```yaml
command: 
  - /bin/sh
  - -ec
  - >-
    mysql -u root -p$MYSQL_ROOT_PASSWORD -e 'SELECT 1'
```

***Note:*** We can use $ to use variable.

## Placeholders

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Values.service.name }}
spec:
  selector:
   app: {{ .Values.service.app }}
   ports: 
   - protocol: TCP
     port: {{ .Values.service.port }}
     targetPort: {{ .Values.service.targetPort }}
```

***Note:*** {{ }} Is used for Placeholder to use dynamic value instead of using environment variable

## Multiple Document

```yaml

apiVersion: v1
kind: Service
metadata:
  name: {{ .Values.service.name }}
spec:
  selector:
   app: {{ .Values.service.app }}
   ports: 
   - protocol: TCP
     port: {{ .Values.service.port }}
     targetPort: {{ .Values.service.targetPort }}

---

apiVersion: v1
kind: ApiService
metadata:
  name: {{ .Values.service.name }}
spec:
  selector:
   app: {{ .Values.service.app }}
   ports: 
   - protocol: TCP
     port: {{ .Values.service.port }}
     targetPort: {{ .Values.service.targetPort }}

```

***Note:*** --- Is used to separate multiple yaml document in single yaml file.
&nbsp;

Author **Jahir Raihan**
&nbsp;

Follow me on &nbsp;  [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jraihan-me/) &nbsp; [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jahirraihan22)
