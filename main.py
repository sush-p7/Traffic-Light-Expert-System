from experta import*
#Define the knowledge base
class TrafficLigthExpertSystem(KnowledgeEngine):
    @DefFacts()
    def initial_facts(self):
        yield Fact(color=None)

    @Rule(Fact(color=None))
    def ask_color(self):
        color = input("Enter your color(red,green,yellow)  :  ")
        self.declare(Fact(color=color.lower()))

    @Rule(Fact(color="red"))
    def rule_red(self):
        print("stop. the trafic light is red")


    @Rule(Fact(color="yellow"))
    def rule_yellow(self):
        print("prepare to stop. the trafic light is yellow")

    @Rule(Fact(color="green"))
    def rule_green(self):
        print("Go. the trafic light is green")

#crete an instance of the expert system
traffic_light_system = TrafficLigthExpertSystem()
traffic_light_system.reset()
traffic_light_system.run()