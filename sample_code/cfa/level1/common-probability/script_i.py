import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.interpolate import interp1d

# Plot Settings
y_scale = 0.95
# Portfolio A parameters
mean_a = 0.12
std_a = 0.18

# Portfolio B parameters
mean_b = 0.10
std_b = 0.12

# Standard normal parameters
z_a = (0 - mean_a) / std_a
z_b = (0 - mean_b) / std_b

# Create the figure and axis objects
fig, axs = plt.subplots(2, 2, figsize=(10, 8), gridspec_kw={'height_ratios': [1, 1]})
((ax1, ax2), (ax3, ax4)) = axs

# Plot normally distributed returns for Portfolio A
x_a = np.linspace(-0.3, 0.6, 2000)
y_a = norm.pdf(x_a, mean_a, std_a)
# Interpolate the y-value of the intersection point
interp_a = interp1d(x_a, y_a)
y_intersect_0_a = interp_a(0)
y_intersect_mean_a = interp_a(mean_a)
axs[0, 0].plot(x_a, y_a, color='blue')
axs[0, 0].fill_between(x_a, 0, y_a, where=(x_a <= 0), color='blue', alpha=0.5)
axs[0, 0].axvline(x=0, color='black', linestyle='-', ymax=y_scale * y_intersect_0_a / max(y_a))
axs[0, 0].axvline(
    x=mean_a,
    color='black',
    linestyle='-', ymax=y_scale * y_intersect_mean_a/max(y_a),
    lw=1)

axs[0, 0].set_title(r'Portfolio A: E(R) = 12%, $σ_A$ = 18%')
axs[0, 0].annotate(
    'Probability of\nreturns < 0%\n- i.e. short fall risk',
    xytext=(-0.2, 1.4),
    xy=(-0.1, 0.6),
    arrowprops=dict(arrowstyle='->'),
    color='blue',
    ha='center',
    fontsize=8,
)
axs[0, 0].text(0, -0.6, r'$SFR_A = \frac{12 - 0}{18} = 0.667$', fontsize=12)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(True)
ax1.set_yticks([])
ax1.set_xticks([0, 0.12], ['0%', '12%'])
ax1.set_ylim(bottom=0)

# Plot normally distributed returns for Portfolio B
x_b = np.linspace(-0.2, 0.4, 1000)
y_b = norm.pdf(x_b, mean_b, std_b)
y_intersect_0_b = norm.pdf(0, mean_b, std_b)
y_intersect_mean_b = norm.pdf(mean_b, mean_b, std_b)
axs[0, 1].plot(x_b, y_b, color='blue')
axs[0, 1].fill_between(x_b, 0, norm.pdf(x_b, mean_b, std_b), where=(x_b <= 0), color='blue', alpha=0.5)
axs[0, 1].axvline(x=0, color='black', linestyle='-', ymax=y_intersect_0_b/max(y_b) * y_scale)
axs[0, 1].axvline(x=mean_b, color='black', linestyle='-', lw=1, ymax=y_intersect_mean_b/max(y_b) * y_scale)
axs[0, 1].set_title(r'Portfolio B: E(R) = 10%, $σ_B$ = 12%')
axs[0, 1].text(0, -0.9, r'$SFR_B = \frac{10 - 0}{12} = 0.833$', fontsize=12)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(True)
ax2.set_yticks([])
ax2.set_xticks([0, 0.1], ['0%', '10%'])
ax2.set_ylim(bottom=0)

# Plot standard normal for Portfolio A
x_std_a = np.linspace(-3, 3, 1000)
y_std_a = norm.pdf(x_std_a)
axs[1, 0].plot(x_std_a, y_std_a, color='blue')
axs[1, 0].fill_between(x_std_a, 0, y_std_a, where=(x_std_a <= z_a), color='blue', alpha=0.5)
axs[1, 0].axvline(x=z_a, color='black', linestyle='-', ymax=(norm.pdf(z_a) / max(y_std_a)) * y_scale)
axs[1, 0].axvline(x=0, color='black', linestyle='-', lw=1, ymax=norm.pdf(0) / max(y_std_a) * y_scale)
axs[1, 0].annotate(
    '25.14%',
    xytext=(-2.5, 0.1),
    xy=(-1.5, 0.05),
    arrowprops=dict(arrowstyle='->'),
    color='blue',
    ha='center',
    fontsize=8,
)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.spines['bottom'].set_visible(True)
ax3.set_yticks([])
ax3.set_xticks([-0.67, 0], ['-0.67', '0'])
ax3.set_ylim(bottom=0)

# Plot standard normal for Portfolio B
x_std_b = np.linspace(-3, 3, 1000)
y_std_b = norm.pdf(x_std_b)
axs[1, 1].plot(x_std_b, y_std_b, color='blue')
axs[1, 1].fill_between(x_std_b, 0, y_std_b, where=(x_std_b <= z_b), color='blue', alpha=0.5)
axs[1, 1].axvline(x=z_b, color='black', linestyle='-', ymax=norm.pdf(z_b) /max(y_std_b) * y_scale)
axs[1, 1].axvline(x=0, color='black', linestyle='-', ymax=norm.pdf(0) / max(y_std_b) * y_scale, linewidth=1)
axs[1, 1].annotate(
    '20.33%',
    xytext=(-2.5, 0.1),
    xy=(-1.5, 0.05),
    arrowprops=dict(arrowstyle='->'),
    color='blue',
    ha='center',
    fontsize=8,
)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.spines['left'].set_visible(False)
ax4.spines['bottom'].set_visible(True)
ax4.set_yticks([])
ax4.set_xticks([-0.83, 0], ['-0.83', '0'])
ax4.set_ylim(bottom=0)

fig.text(0.05, 0.95, 'A. Normally Distributed Returns', ha='left', fontsize=12)
fig.text(0.05, 0.42, 'B. Standard Normal', ha='left', fontsize=12)

plt.tight_layout(rect=[0, 0, 1, y_scale], h_pad=5)
plt.savefig('figureI.png', transparent=True)
plt.show()