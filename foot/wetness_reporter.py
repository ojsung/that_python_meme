class Style_Text:
    PURPLE='\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    DEF = '\033[1;37;0m'
    BOLD = '\033[1;37;48m'
    UNDER = '\033[4;37;48m'


    def add_color(self, report: str, color: str) -> str:
        return f'{color}{report}{self.DEF}'
