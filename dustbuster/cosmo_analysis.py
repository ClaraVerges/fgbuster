""" Tools for cosmological analysis

"""

def basic_r_estimation(Cl_BB, model_args, model_kwargs, logL_kwargs)
    """ Estimate r given a BB angular power spectrum

    """
    Cl_ev = _BB_evaluator(*model_args, **model_kwargs)
    fun = lambda r: - logL(Cl_BB, Cl_ev(r), **logL_kwargs) - _positive_prior(x)
    res = sp.optimize.minimize(fun, 0)
    res.Sigma = numdifftools.Hessian(fun)(res.x)
    return res


def _load_tensor():
    # Load tensor BB spectrum for r = 1 from pysm


def _load_lensing():
    # Load the lensing BB spectrum for A_lens = 1 from pysm


def _BB_evaluator(Gl, binning=None, A_lens=1.):
    lensing = _bin(_load_lensing() * lensing, binning) * A_lens
    tensor = _bin(_load_tensor(), binning)
    return lambda r: lensing + Gl + r * tensor


def _bin(cl, binning):
    # Bin Cl according to binning

def _positive_prior(x):
    if x < 0:
        return - np.inf
    else:
        return 0.

def logL(Cl, model_Cl, dof):
    return - 0.5 * np.sum(dof * (Cl / Cl_model + np.log(Cl_model)))


