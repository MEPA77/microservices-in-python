# microservices-in-python
1.-Install Pyton 
2.-Create Python virt env
    -python -m venv PathOrFileName
    -https://docs.python.org/3/library/venv.html
3.- Install Python vscode Extension
4.-Sample flask App
    -https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
5.-jinja templating for dynamic web pages
    -use folder /src/templates to safe the html files
    -use double brackets on the html for dynamic content:
        <h2>Rsponse from Host {{hostname}}, IP:{{ip}}</h2>
    -on the route, use return render_template('index.html', hostname= hostname, ip = ip)
6.-Freeze python depoendemcies with pip
6.1.-Install Minikube
    -https://minikube.sigs.k8s.io/docs/start/
    -on powershell run: minikube start
    -check if the minikube docker image is active, on powershell: docker ps
7.- Build docker image using dockerfile
    -Create Dockerfile
    -Create .dockerignote file
    -add the virtual environment to the ignore file
    -Create dockerImage
        -docker build -t imagename:tagname .
    -Run Docker containter
        -docker run -d -p 80:5000 --name web webapp1.0
8.-Write kubernetes manifest files for the app
9.- Create Helm chart
  
SOURCE for Tutorial
https://youtu.be/SdTzwYmsgoU