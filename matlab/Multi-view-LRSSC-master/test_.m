clear;
addpath(genpath(cd))

load 3-sources
%keys=[ "120212", "120515", "128127", "123117", "116221", "118528", "115825", "125525", "126325", "122620", "123521", "128935", "117324", "121416", "122317", "117930", "116524", "124624", "119126", "124220", "126628", "128632", "115219", "123925", "129129", "119833", "127933", "119732", "117122", "128026", "121921", "114621", "115017", "116726", "121618", "124826", "127327", "114823", "118730", "123420", "127630", "124422", "129028", "120717", "115320", "118932", "118124", "118023", "122822", "129331", "118225", "123824"]
keys=["114621","114823","115017","115219","115320","115825","116221","116524","116726","117122","117324","117930","118023","118124","118225","118528","118730","118932","119126","119732","119833","120111","120212","120515","120717","121416","121618","121921","122317","122620","122822","123117","123420","123521","123824","123925","124220","124422","124624","124826","125525","126325","126628","127327","127630","127933","128026","128127","128632","128935","129028","129129","129331"]
%keys=["123117","120212","118932","115825"]
for key=keys
   key
   stru
   t_mat=importdata("D:/PROJECT\CODE/matfile/index_fixed/structual_matrix_1/"+key+".mat");
   func_mat=importdata("D:/PROJECT/CODE/matfile/index_fixed/functional_matrix/"+key+".mat");
 


   % X{1} = bbc;+
   % X{2} = guardian;
   % X{3} = reuters;


   X{1}=struct_mat;
   X{2}=func_mat;

   k = 6;
   num_views = 2;
   num_iter = 100;

   %% Linear kernel multi-view LRSSC

   fprintf('\nPairwise multiview LRSSC\n');
   opts.mu = 10^2;
   lambda1 = 0.3;
   lambda3 = 0.3;      
   opts.lambda = [lambda1 (1-lambda1) lambda3];
   opts.noisy = true;

   A = pairwise_MLRSSC(X, opts); % joint affinity matrix
   %[best.CA best.F best.P best.R best.nmi best.AR] = spectral_clustering(A, k, truth);
   %best
   save("D:/PROJECT\CODE/matfile/index_fixed/fix_result_1/"+key+".mat","A") 
end