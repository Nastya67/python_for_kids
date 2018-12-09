import psutil, time
import subprocess


def test(text, fname="tmp", fout="out", ferr="err"):
    fname += ".py"
    fil = open(fname, "w")
    fil.write(text)
    fil.close()
    out = open(fout+".txt", "w")
    err = open(ferr+".txt", "w")
    subp = subprocess.Popen(["python", fname], stdout=out, stderr=err)

    p = psutil.Process(subp.pid)
    try:
        p.wait(timeout=2)
    except psutil.TimeoutExpired:
        p.kill()
        return "", "Some error. Please, try again!"
    except psutil.AccessDenied:
        p.kill()
        return "", "Some error. Please, try again!"
    else:
        out.close()
        err.close()
        fres = open(fout+".txt", "r")
        res = fres.read()
        fres.close()
        ferror = open(ferr+".txt", "r")
        errtxt = ferror.read()
        ferror.close()
        return res.strip(), errtxt.strip()
