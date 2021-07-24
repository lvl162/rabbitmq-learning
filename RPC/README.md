## 1. Compile

```
javac -cp amqp-client-5.7.1.jar RPCClient.java RPCServer.java
```

## 2. Run

```

java -cp ".;amqp-client-5.7.1.jar;slf4j-api-1.7.26.jar;slf4j-simple-1.7.26.jar" RPCClient

```

```

java -cp ".;amqp-client-5.7.1.jar;slf4j-api-1.7.26.jar;slf4j-simple-1.7.26.jar" RPCServer

```

## 3. List

```
rabbitmqctl list_queues
```

```
rabbitmqctl list_bindings

```

```
rabbitmqctl list_exchanges

```
