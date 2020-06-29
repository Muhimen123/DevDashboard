# DevDashboard

As the name suggests, dev dashboard is a CLI verstion of the [dev.to](https://www.dev.to) dashboard. It aims to help the writers to have a close look at few public data such as total post views, comments, reactions and many more. Why would anyone use a CLI instead of a awesome UI? Well, that depends. Primarily, it has some feature for data visualization. So, for those who loves data like me, it might be a useful thing.

***

# Installation

If you are using mac or linux then you are 50% done. However, if you are using windows or if you don't have python installed in your machine I will highly incourage you to install and setup python properly in your machine from the official [python website](https://www.python.org/).

Now, to finish rest of the 50% installation, you will need to download the following python modules. Make sure you have [pip](https://www.liquidweb.com/kb/install-pip-windows/) installed.

- matplotlib
- pandas
- numpy
- requests

To install the libraries just type the followings

```bash
pip install matplotlib
pip install requests
pip install pandas
```

(You don't need to install numpy separately as matplotlib will download them)

Now, you will need to get an api key from [Dev](https://docs.dev.to/api/#section/Authentication). Once you have the API key, open `dev_api.py` script in any text editor you want. You will find a code like this.

```python
headers = {
    "api-key": apikey # Enter the API key
}
```

Enter the API key that you recently generated, you are now all set!

***

# Getting started
The program itself isn't that much complicated. You can learn how to use it all by yourself. However, if you want to have a more detailed instruction, I recommend you to read this [blog post](https://dev.to/muhimen123/i-made-a-data-analyzer-for-dev-to-3pol). Things are explained quite broadly here.

## Thank you for your time

