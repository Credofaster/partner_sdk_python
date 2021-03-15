# Getting started

Buy Airtime on the most simplistic System. We abstract all the nitty-gritty leaving you with just the option to specify the account number to receive airtime and how much. 

We guarantee 95% uptime, 99% reliability.

Just Request and we will make sure you get, in realtime. If not, you will be notified immediately by events.

Now, what Credo is faster that Credofaster!

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Credofaster%20Partner%20Api-Python)


## How to Use

The following section explains how to use the Credofasterpartnerapi SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Credofaster%20Partner%20Api-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Credofaster%20Partner%20Api-Python&projectName=credofasterpartnerapi)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Credofaster%20Partner%20Api-Python&projectName=credofasterpartnerapi)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=Credofaster%20Partner%20Api-Python&projectName=credofasterpartnerapi)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from credofasterpartnerapi.credofasterpartnerapi_client import CredofasterpartnerapiClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Credofaster%20Partner%20Api-Python&libraryName=credofasterpartnerapi.credofasterpartnerapi_client&projectName=credofasterpartnerapi&className=CredofasterpartnerapiClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Credofaster%20Partner%20Api-Python&libraryName=credofasterpartnerapi.credofasterpartnerapi_client&projectName=credofasterpartnerapi&className=CredofasterpartnerapiClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| api_key | Assigned APIKey |
| client_id | Assigned ClientId |



API client can be initialized as following.

```python
# Configuration parameters and credentials
api_key = 'XXXX-XXXX-XXXX-XXXX' # Assigned APIKey
client_id = 'ABCDEDFG1234' # Assigned ClientId

client = CredofasterpartnerapiClient(api_key, client_id)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [MainController](#main_controller)
* [EventsController](#events_controller)

## <a name="main_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MainController") MainController

### Get controller instance

An instance of the ``` MainController ``` class can be accessed from the API Client.

```python
 main_controller = client.main
```

### <a name="airtime_request"></a>![Method: ](https://apidocs.io/img/method.png ".MainController.airtime_request") airtime_request

> Request Airtime Purchase

```python
def airtime_request(self,
                        request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = PartnerAirtimeRequest()

result = main_controller.airtime_request(request)

```


### <a name="airtime_balance"></a>![Method: ](https://apidocs.io/img/method.png ".MainController.airtime_balance") airtime_balance

> Gets the current Working Balance. 
> Balance is SIGNED

```python
def airtime_balance(self)
```

#### Example Usage

```python

result = main_controller.airtime_balance()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="events_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EventsController") EventsController

### Get controller instance

An instance of the ``` EventsController ``` class can be accessed from the API Client.

```python
 events_controller = client.events
```

### <a name="register_callback"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.register_callback") register_callback

> A callback to receive the below Callbacks

```python
def register_callback(self,
                          request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = RegisterCallbackRequest()

result = events_controller.register_callback(request)

```


### <a name="client_event_feedback"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.client_event_feedback") client_event_feedback

> *Tags:*  ``` Skips Authentication ``` 

> You are required to provide a HTTP/HTTPS endpoint, to which we will publish various events. 
> 
> This Endpoint will be hosted on the CLIENT's Environment. If no endpoint is provided, we are not liable to any missing events. 
> 
> NOTE: A DETAILED PDF of all Events is shared on request. It contains application events, System Health Events and Alerts on the same.

```python
def client_event_feedback(self,
                              payload_to_receive)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| payloadToReceive |  ``` Required ```  | Sample Payload: {"EventId":"123456789","EventType":"QUEUED","RequestId":"A09797a11e2564061b859781b18bb34dd","EventData":{}} |



#### Example Usage

```python
payload_to_receive_value = "{\"EventId\":\"123456789\",\"EventType\":\"QUEUED\",\"RequestId\":\"A09797a11e2564061b859781b18bb34dd\",\"EventData\":{}}"
payload_to_receive = json.loads(payload_to_receive_value)

result = events_controller.client_event_feedback(payload_to_receive)

```


[Back to List of Controllers](#list_of_controllers)



