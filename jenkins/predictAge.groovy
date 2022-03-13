import groovy.json.JsonSlurper

properties([
    parameters([
        string(name: 'name', defaultValue: 'Jack'),
    ])
])    

def predictAge(String name) {
    def get = new URL("https://api.agify.io/?name=${name}").openConnection();
    def getRC = get.getResponseCode();
    if (getRC.equals(200)) {
        def slurper = new groovy.json.JsonSlurper();
        def result = slurper.parseText(get.getInputStream().getText());
        return result.age;
    } else {
        throw new Exception("HTTP Request to api.agify.io failed");
    }
}

node {
    stage('Predict age') { // for display purposes
        echo "Predicting age for ${params.name}"
        echo "Predicited age: ${predictAge(params.name)}"
    }
}
