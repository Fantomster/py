# Use four different models to compute initial prediction
preds_a = model_a.predict(x_val)
preds_b = model_b.predict(x_val)
preds_c = model_c.predict(x_val)
preds_d = model_d.predict(x_val)

# This new prediction array should be more accurate than any of the initial ones
final_preds = 0.25 * (preds_a + preds_b + preds_c + preds_d)

preds_a = model_a.predict(x_val)
preds_b = model_b.predict(x_val)
preds_c = model_c.predict(x_val)
preds_d = model_d.predict(x_val)

# Nelder-Mead
# These weights (0.5, 0.25, 0.1, 0.15) are assumed to be learned empirically
final_preds = 0.5 * preds_a + 0.25 * preds_b + 0.1 * preds_c + 0.15 * preds_d