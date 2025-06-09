import matplotlib.pyplot as plt
import plotly.graph_objects as go

def plot_distances(distances, label):
    plt.plot(distances, label=label)
    plt.xlabel('Time step')
    plt.ylabel('Distance (km)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_orbit_3d(positions_list, labels=None):
    """
    Create an interactive 3D scatter plot of satellite positions using Plotly.

    Args:
        positions_list (List[List[Tuple[float, float, float]]]):
            A list of position lists, each containing (x, y, z) tuples over time.
        labels (List[str], optional):
            Optional labels for each satellite trace.
    """
    fig = go.Figure()
    for idx, positions in enumerate(positions_list):
        xs, ys, zs = zip(*positions)
        fig.add_trace(
            go.Scatter3d(
                x=xs, y=ys, z=zs,
                mode='lines+markers',
                name=labels[idx] if labels else f'Satellite {idx}',
                marker=dict(size=3),
                line=dict(width=2)
            )
        )
    fig.update_layout(
        scene=dict(
            xaxis_title='X (km)',
            yaxis_title='Y (km)',
            zaxis_title='Z (km)'
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )
    fig.show()