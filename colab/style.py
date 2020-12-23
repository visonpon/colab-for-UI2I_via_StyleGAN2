
%tensorflow_version 1.x

!git clone https://github.com/HideUnderBush/UI2I_via_StyleGAN2
  
!cd  /content/UI2I_via_StyleGAN2/

!git clone https://github.com/NVlabs/stylegan2
  
!pip install ninja

from google.colab import drive
drive.mount('/content/drive/', force_remount=True)

#change weights from pkl to pt use convert_weight.py from styglegan2
!python convert_weight.py --repo ../drive/MyDrive/550000.pt %also can change to stylegan2-ffhq-config-f.pkl 

#get factor.pt
!python closed_form_factorization.py --ckpt ../drive/MyDrive/550000.pt --out factor.pt

#generate style image
!python projector_factor.py --ckpt ../drive/MyDrive/550000.pt --fact factor_5.pt ./sample/000000.png
