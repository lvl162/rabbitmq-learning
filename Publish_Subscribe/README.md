## Compile

```
javac -cp amqp-client-5.7.1.jar ReceiveLogs.java EmitLog.java
```

## Run

```
java -cp ".;amqp-client-5.7.1.jar;slf4j-api-1.7.26.jar;slf4j-simple-1.7.26.jar" ReceiveLogs

```

```
java -cp ".;amqp-client-5.7.1.jar;slf4j-api-1.7.26.jar;slf4j-simple-1.7.26.jar" EmitLog

```

Listing bindings
You can list existing bindings using, you guessed it,

```
rabbitmqctl list_queues
rabbitmqctl list_bindings
rabbitmqctl list_exchanges
```
