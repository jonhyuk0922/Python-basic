import argparse 
""" 
#위치 인자 소개
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",type=int)
args = parser.parse_args()
print(args.square**2) """

"""
#옵션 인자 소개
parser = argparse.ArgumentParser()
parser.add_argument("--verbose",help="increase output verbosity",action="store_true") #action 지정안하면 False
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
"""

"""
#짧은 옵션
parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose",help="increase output verbosity",action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")

"""
"""
#위치 및 옵션 인자 결합하기
parser= argparse.ArgumentParser()
parser.add_argument("square",type=int,help = "display a square of a given number")
parser.add_argument("-v","--verbosity", type=int,choices=[0,1,2],help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity ==2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer) """

"""
#상세도를 다루는 다른 접근법
parser =argparse.ArgumentParser()
parser.add_argument("square",type=int,help="display the square of a given number")
parser.add_argument("-v","--verbosity",action="count",default=0,help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity >=2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity >=1:
    print(f"{args.square}^2 =={answer}")
else:
    print(answer)
"""
"""

#조금 더 발전시키기
parser = argparse.ArgumentParser()
parser.add_argument("x",type=int,help="the base")
parser.add_argument("y",type=int,help="the exponent")
parser.add_argument("-v","--verbosity",action="count",default=0)
args = parser.parse_args()
answer = args.x ** args.y
if args.verbosity >= 2:
    print(f"Running '{__file__}'")
if args.verbosity >= 1:
    print(f"{args.x}^{args.y}=={answer}")
else:
    print(answer)

"""

#충동하는 옵션들 
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v","--verbose",action="store_true")
group.add_argument("-q","--quiet",action="store_true")
parser.add_argument("x",type=int,help="the base")
parser.add_argument("y",type=int,help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")
