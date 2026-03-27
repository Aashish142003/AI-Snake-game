from snake.game import Game, GameConf, GameMode

greedy = "GreedySolver"
hamilton = "HamiltonSolver"

benchmark = GameMode.BENCHMARK
conf = GameConf()
conf.solver_name = greedy
conf.mode = benchmark
print("Solver: %s " % (conf.solver_name))
print("Mode: %s" %(conf.mode))
Game(conf).run()
