## 1. Compile

```
javac -cp amqp-client-5.7.1.jar ReceiveLogsTopics.java EmitLogTopics.java
```

## 2. Run

```

java -cp ".;amqp-client-5.7.1.jar;slf4j-api-1.7.26.jar;slf4j-simple-1.7.26.jar" ReceiveLogsTopics kern.\*

```

```

java -cp ".;amqp-client-5.7.1.jar;slf4j-api-1.7.26.jar;slf4j-simple-1.7.26.jar" ReceiveLogsTopics "#"

```

```

java -cp ".;amqp-client-5.7.1.jar;slf4j-api-1.7.26.jar;slf4j-simple-1.7.26.jar" ReceiveLogsTopics \*.critical

```

```

java -cp ".;amqp-client-5.7.1.jar;slf4j-api-1.7.26.jar;slf4j-simple-1.7.26.jar" ReceiveLogsTopics "kern._" "_.critical"

```

```

java -cp ".;amqp-client-5.7.1.jar;slf4j-api-1.7.26.jar;slf4j-simple-1.7.26.jar" ReceiveLogsTopics \*.critical

```

```
java -cp ".;amqp-client-5.7.1.jar;slf4j-api-1.7.26.jar;slf4j-simple-1.7.26.jar" EmitLogTopics "kern.critical" "A critical kernel error"

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
