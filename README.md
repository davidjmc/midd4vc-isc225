<h1 align="center">Midd4VC: A Middleware for Vehicular Cloud Computing</h1>

## 📝 Summary <a name="summary"></a>

- [📖 About](#about)
- [🏁 Getting Started](#getting_started)
- [📱 Usage](#usage)
- [⛏️ Technologies Used](#built_using)

## 📖 About <a name = "about"></a>

Midd4VC (Middleware for Vehicular Cloud) is a lightweight and extensible middleware designed to support the creation and management of vehicular clouds. It mediates communication between vehicles and VCC entities (e.g., application clients and roadside units), distributing and coordinating jobs among them. The current implementation adopts MQTT (Message Queuing Telemetry Transport), a widely used lightweight messaging protocol, and includes mechanisms for reconnection, message handling, and concurrent job execution.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will help you get a copy of this project and run it on your local machine for development and testing purposes.

Clone this repository to your local machine:

```bash
git clone https://github.com/davidjmc/midd4vc-isc225.git
```

Navigate into the project directory:

```bash
cd midd4vc-isc225
```

This software was developed to run in a Linux environment.

### Prerequisites

To run the project, you will need to have Python3 and pip3 installed on your machine. You can download Python3 [here](https://www.python.org/) or install it using the following commands:

```bash
# Install Python and pip:
sudo apt install python3 python3-pip
```

Additionally, install the EMQX:

```bash
# Install the EMQX apt repository:
curl -s https://packagecloud.io/install/repositories/emqx/emqx-enterprise5/script.deb.sh | sudo bash

# Install EMQX:
sudo apt-get install emqx

# Start EMQX:
sudo systemctl start emqx
```

### Installation

After cloning the repository, enter the project directory and install the dependencies:

```bash
pip3 install paho-mqtt==1.6.1
```

## 📱 Usage <a name="usage"></a>

Make sure the EMQX broker is running.

### Running the Server

To run the server, use the command below:

```bash
cd  server/

python3 Midd4VCServer.py
```

### Running the Client

To run the client, use the command below:

```bash
cd  client/

# To run vehicle node, use:
python3 vehicle.py

# To run application client, use:
python3 application.py
```

### Results

The results are stored in the `evaluation`. The experiment results were saved as CSV files and charts as pdf, which can be used for analysis and data visualization.

## ⛏️ Technologies Used <a name = "built_using"></a>

- [Python3](https://www.python.org/) - Programming language
- [EMQX](https://www.emqx.com/en) - MQTT messaging platform
- [Paho MQTT](https://pypi.org/project/paho-mqtt/) - MQTT Client
