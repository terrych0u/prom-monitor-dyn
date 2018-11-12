# prom-monitor-dyn
Simple stack of grafana+promethues+consul with monitor dynamic target 

Using for demonstration bout how to monitor your instance when auto-auto-scaling happened and you would'wouldn't change any config on promethues, it will auto detect the new monitor target, and show on grafana dashboard.

---

## How to use it

#### Monitor Server
Launch an instance as main monitor server on AWS, but it will require the specific tag name on instance. 

Please add the following tags on instance:

```
Name     vaule
service  consul
```

After that, you can runing following commend to launch monitor:

```bash
docker-compose -f docker-compose.yml up -d
```

#### Monitor Target/Clients

Before running agent's docker-compose, we need to create consul's config first, it will done by using **agent_config_gen.py**

Following commend will help you to do that:

```bash
pip install -r requirement.txt

python agent_config_gent.py
```

***Notice : this scripts only running on python 3***

After that, you can runing following commend to launch clients:

```bash
docker-compose -f docker-compose-agent.yml up -d
```

---

Just don't forget to setup security group and config your own grafana dashboard.

You also can lanuch other instance to running Monitor Target/Clients docker compose, 
simulate auto-scaling happened, to see the result of dashboard will auto showing new instance target or not.

Enjoy it