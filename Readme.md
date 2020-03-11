Problem questions
=================

```
How do you map the network rules to each platform i.e. how are the rules applied on each platform and to what types of resources on that platform?  
``` 

The google cloud sdk offers the possibility to write a json with the firewall
body which is passed to an api function. In the body json you also specify the type
of resource you are using i.e. compute engine

```
What are the differences between the platforms from a networking perspective? How does this impact your ability to create an abstraction across the platforms?
```

Unfortunateley, I only implemented it for google compute engine. Each cloud provider
provides an sdk upon I can built the same abstraction as for google cloud.

```
How fine grained do you provide control over network flow? How would you go about extending this for finer grain control?  Per instance? Per group? Per network?  
```

At this moment, I can apply per instance restrictions. The granularity is at the 
lowest level.