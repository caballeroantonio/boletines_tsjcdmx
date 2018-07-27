import sys,string,os;
import re;

class Boletin():
    header_tsj = re.compile(r'^TSJ CIUDAD\n$');
    header_cdmx = re.compile(r'^DE MÉXICO\n$');
    header_fecha = re.compile(r'^BOLETÍN JUDICIAL No\..*\n$');
    header_no_page = re.compile(r'^\d+\n$');
    begin_salas = re.compile(r'^Salas\n$');
    begin_sentencias = re.compile(r'^SENTENCIAS\n$');
    end_acdo = re.compile(r'^.*Acdos{0,1}\.\n$');
#    en Cuad. Amp.
    
    
    def doit(self):
        os.close(0)
        os.close(1)
        sys.stdin = open(sys.argv[1],"r");
        sys.stdout = open(sys.argv[2],"w");
        
        self.input = sys.stdin;
        
        lines = [];
        while True:
            line = self.input.readline();
            if not line:
                break;
                
                
            if self.header_tsj.match(line):
                continue;
            elif self.header_cdmx.match(line):
                continue;
            elif self.header_fecha.match(line):
                continue;
            elif self.header_no_page.match(line):
                sys.stdout.write('<pag>'+line[:-1]+'</pag>\r\n');
                continue;
            elif self.begin_salas.match(line):
                sys.stdout.write('<salas>'+line[:-1]+'</salas>\r\n');
                continue;
            elif self.begin_sentencias.match(line):
                sys.stdout.write('<sentencias>'+line[:-1]+'</sentencias>\r\n');
                continue;
                
            lines.append(line[:-1]);#.replace('\n','');
            if self.end_acdo.match(line):
                sys.stdout.write('<acdo>'+'\t'.join(lines)+'</acdo>\r\n');
                
                lines.clear();
        return True;

def main():
  boletin = Boletin();
  print(boletin.doit());



if __name__ == '__main__':
  main()
