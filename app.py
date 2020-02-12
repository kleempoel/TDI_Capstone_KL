from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/gwas')
def gwas():
  return render_template('gwas.html')
  
@app.route('/plink_sim_RF_1M')
def plink_sim_RF_1M():
  return render_template('plink_sim_RF_1M.html')

if __name__ == '__main__':
  app.run(port=5000)
